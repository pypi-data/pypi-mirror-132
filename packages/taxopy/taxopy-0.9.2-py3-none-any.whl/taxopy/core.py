# -*- coding: utf-8 -*-
#
#   This file is part of the taxopy package, available at:
#   https://github.com/apcamargo/taxopy
#
#   Taxopy is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with this program. If not, see <https://www.gnu.org/licenses/>.
#
#   Contact: antoniop.camargo@gmail.com

import os
import tarfile
import urllib.request
from typing import List

from taxopy.exceptions import DownloadError, ExtractionError, TaxidError


class TaxDb:
    """
    Create an object of the TaxDb class.

    Parameters
    ----------
    taxdb_dir : str, optional
        A directory to download NCBI's taxonomy database files to. If the
        directory does not exist it will be created.
    nodes_dmp : str, optional
        The path for a pre-downloaded `nodes.dmp` file. If both `nodes.dmp` and
        `names.dmp` are supplied NCBI's taxonomy database won't be downloaded.
    names_dmp : str, optional
        The path for a pre-downloaded `names.dmp` file. If both `names.dmp` and
        `nodes.dmp` are supplied NCBI's taxonomy database won't be downloaded.
    merged_dmp : str, optional
        The path for a pre-downloaded `merged.dmp` file.
    keep_files : bool, default True
        Keep the `nodes.dmp` and `names.dmp` files after the TaxDb object is
        created. If `taxdb_dir` was supplied the whole directory will be deleted.
        By default, the files are deleted.

    Attributes
    ----------
    taxid2name : dict
        A dictionary where the keys are taxonomic identifiers and the values are
        their corresponding names.
    taxid2parent: dict
        A dictionary where the keys are taxonomic identifiers and the values are
        the taxonomic identifiers of their corresponding parent taxon.
    taxid2rank: dict
        A dictionary where the keys are taxonomic identifiers and the values are
        their corresponding ranks.
    oldtaxid2newtaxid: dict
        A dictionary where the keys are legacy taxonomic identifiers and the
        values are their corresponding new identifiers. If pre-downloaded
        `nodes.dmp` and `names.dmp` files were provided but the `merged.dmp`
        file was not supplied, this attribute will be `None`.

    Raises
    ------
    DownloadError
        If the download of the taxonomy database fails.
    ExtractionError
        If the decompression of the taxonomy database fails.
    """

    def __init__(
        self,
        *,
        taxdb_dir: str = None,
        nodes_dmp: str = None,
        names_dmp: str = None,
        merged_dmp: str = None,
        keep_files: bool = False
    ):
        if not taxdb_dir:
            self._taxdb_dir = os.getcwd()
        elif not os.path.isdir(taxdb_dir):
            os.makedirs(taxdb_dir)
            self._taxdb_dir = taxdb_dir
        else:
            self._taxdb_dir = taxdb_dir
        # If `nodes_dmp` and `names_dmp` were not provided:
        if not (nodes_dmp and names_dmp):
            nodes_dmp_path = os.path.join(self._taxdb_dir, "nodes.dmp")
            names_dmp_path = os.path.join(self._taxdb_dir, "names.dmp")
            merged_dmp_path = os.path.join(self._taxdb_dir, "merged.dmp")
            # If the `nodes.dmp` and `names.dmp` files are not in the `taxdb_dir` directory,
            # download the taxonomy from NCBI:
            if not (os.path.isfile(nodes_dmp_path) and os.path.isfile(names_dmp_path)):
                (
                    self._nodes_dmp,
                    self._names_dmp,
                    self._merged_dmp,
                ) = self._download_taxonomy()
            # If `nodes.dmp` and `names.dmp` are found in the `taxdb_dir` directory:
            else:
                self._nodes_dmp, self._names_dmp = nodes_dmp_path, names_dmp_path
                # If `merged.dmp` is not in the `taxdb_dir` directory, set the `_merged_dmp`
                # attribute to `None`:
                self._merged_dmp = (
                    merged_dmp_path if os.path.isfile(merged_dmp_path) else None
                )
        else:
            self._nodes_dmp, self._names_dmp = nodes_dmp, names_dmp
            # If `merged_dmp` was not provided, set the `_merged_dmp` attribute to `None`:
            self._merged_dmp = None if not merged_dmp else merged_dmp
        # If a `merged.dmp` file was provided or downloaded, create the oldtaxid2newtaxid
        # dictionary:
        self.oldtaxid2newtaxid = self._import_merged() if self._merged_dmp else None
        # Create the taxid2parent, taxid2rank, and taxid2name dictionaries:
        self.taxid2parent, self.taxid2rank = self._import_nodes()
        self.taxid2name = self._import_names()
        # If `keep_files` is set to `False`, delete temporary files:
        if not keep_files:
            self._delete_files()

    def _download_taxonomy(self):
        url = "ftp://ftp.ncbi.nlm.nih.gov/pub/taxonomy/taxdump.tar.gz"
        tmp_taxonomy_file = os.path.join(self._taxdb_dir, "taxdump.tar.gz")
        try:
            urllib.request.urlretrieve(url, tmp_taxonomy_file)
        except:
            raise DownloadError(
                "Download of taxonomy files failed. NCBI's server may be offline."
            )
        try:
            with tarfile.open(tmp_taxonomy_file) as tf:
                tf.extract("nodes.dmp", path=self._taxdb_dir)
                tf.extract("names.dmp", path=self._taxdb_dir)
                tf.extract("merged.dmp", path=self._taxdb_dir)
        except:
            raise ExtractionError(
                "Something went wrong while extracting the taxonomy files."
            )
        os.remove(tmp_taxonomy_file)
        return (
            os.path.join(self._taxdb_dir, "nodes.dmp"),
            os.path.join(self._taxdb_dir, "names.dmp"),
            os.path.join(self._taxdb_dir, "merged.dmp"),
        )

    def _import_merged(self):
        oldtaxid2newtaxid = {}
        with open(self._merged_dmp, "r") as f:
            for line in f:
                line = line.split("\t")
                taxid = int(line[0])
                merged = int(line[2])
                oldtaxid2newtaxid[taxid] = merged
        return oldtaxid2newtaxid

    def _import_nodes(self):
        taxid2parent = {}
        taxid2rank = {}
        with open(self._nodes_dmp, "r") as f:
            for line in f:
                line = line.split("\t")
                taxid = int(line[0])
                parent = int(line[2])
                rank = line[4]
                taxid2parent[taxid] = parent
                taxid2rank[taxid] = rank
        if self._merged_dmp:
            for oldtaxid, newtaxid in self.oldtaxid2newtaxid.items():
                taxid2rank[oldtaxid] = taxid2rank[newtaxid]
                taxid2parent[oldtaxid] = taxid2parent[newtaxid]
        return taxid2parent, taxid2rank

    def _import_names(self):
        taxid2name = {}
        with open(self._names_dmp, "r") as f:
            for line in f:
                line = line.split("\t")
                if line[6] == "scientific name":
                    taxid = int(line[0])
                    name = line[2]
                    taxid2name[taxid] = name
        if self._merged_dmp:
            for oldtaxid, newtaxid in self.oldtaxid2newtaxid.items():
                taxid2name[oldtaxid] = taxid2name[newtaxid]
        return taxid2name

    def _delete_files(self):
        os.remove(self._nodes_dmp)
        os.remove(self._names_dmp)
        if self._merged_dmp:
            os.remove(self._merged_dmp)
        if not os.listdir(self._taxdb_dir) and self._taxdb_dir != os.getcwd():
            os.rmdir(self._taxdb_dir)


class Taxon:
    """
    Create an object of the Taxon class.

    Parameters
    ----------
    taxid : int
        A NCBI taxonomic identifier.
    taxdb : TaxDb
        A TaxDb object.

    Attributes
    ----------
    taxid : int
        The NCBI taxonomic identifier the object represents (e.g., 9606).
    name: str
        The name of the taxon (e.g., 'Homo sapiens').
    rank: str
        The rank of the taxon (e.g., 'species').
    legacy_taxid: bool
        A boolean that represents whether the NCBI taxonomic identifier was
        merged to another identifier (`True`) or not (`False`). If pre-downloaded
        `nodes.dmp` and `names.dmp` files were provided to build `taxdb` but the
        `merged.dmp` file was not supplied, this attribute will be `None`.
    taxid_lineage: list
        An ordered list containing the taxonomic identifiers of the whole lineage
        of the taxon, from the most specific to the most general.
    name_lineage: list
        An ordered list containing the names of the whole lineage of the taxon,
        from the most specific to the most general.
    rank_taxid_dictionary: dict
        A dictionary where the keys are named ranks and the values are the taxids
        of the taxa that correspond to each of the named ranks in the lineage.
    rank_name_dictionary: dict
        A dictionary where the keys are named ranks and the values are the names
        of the taxa that correspond to each of the named ranks in the lineage.

    Raises
    ------
    TaxidError
        If the input integer is not a valid NCBI taxonomic identifier.
    """

    def __init__(self, taxid: int, taxdb: TaxDb):
        self.taxid = taxid
        if self.taxid not in taxdb.taxid2name:
            raise TaxidError(
                "The input integer is not a valid NCBI taxonomic identifier."
            )
        self.name = taxdb.taxid2name[self.taxid]
        self.rank = taxdb.taxid2rank[self.taxid]
        if taxdb.oldtaxid2newtaxid:
            self.legacy_taxid = self.taxid in taxdb.oldtaxid2newtaxid
        else:
            self.legacy_taxid = None
        self.taxid_lineage = self._find_lineage(taxdb.taxid2parent)
        self.name_lineage = self._convert_to_names(taxdb.taxid2name)
        (
            self.rank_taxid_dictionary,
            self.rank_name_dictionary,
        ) = self._convert_to_rank_dictionary(taxdb.taxid2rank, taxdb.taxid2name)

    def __repr__(self):
        return " > ".join(reversed(self.name_lineage))

    def _find_lineage(self, taxid2parent):
        lineage = []
        current_taxid = self.taxid
        lineage.append(current_taxid)
        while taxid2parent[current_taxid] != current_taxid:
            current_taxid = taxid2parent[current_taxid]
            lineage.append(current_taxid)
        return lineage

    def _convert_to_names(self, taxid2name):
        return [taxid2name[taxid] for taxid in self.taxid_lineage]

    def _convert_to_rank_dictionary(self, taxid2rank, taxid2name):
        rank_taxid_dictionary = {}
        rank_name_dictionary = {}
        for taxid in self.taxid_lineage:
            rank = taxid2rank[taxid]
            if rank != "no rank":
                rank_taxid_dictionary[rank] = taxid
                rank_name_dictionary[rank] = taxid2name[taxid]
        return rank_taxid_dictionary, rank_name_dictionary


class _AggregatedTaxon(Taxon):
    """
    Create an object of the _AggregatedTaxon class.

    Parameters
    ----------
    taxid : int
        A NCBI taxonomic identifier.
    taxdb : TaxDb
        A TaxDb object.
    agreement : float
        Level of agreement of the aggregated taxonomy.
    aggregated_taxa : list
        List of the aggregated taxonomic identifiers.

    Attributes
    ----------
    taxid : int
        The NCBI taxonomic identifier the object represents (e.g., 9606).
    name: str
        The name of the taxon (e.g., 'Homo sapiens').
    rank: str
        The rank of the taxon (e.g., 'species').
    legacy_taxid: bool
        A boolean that represents whether the NCBI taxonomic identifier was
        merged to another identifier (`True`) or not (`False`).
    taxid_lineage: list
        An ordered list containing the taxonomic identifiers of the whole lineage
        of the taxon, from the most specific to the most general.
    name_lineage: list
        An ordered list containing the names of the whole lineage of the taxon,
        from the most specific to the most general.
    rank_taxid_dictionary: dict
        A dictionary where the keys are named ranks and the values are the taxids
        of the taxa that correspond to each of the named ranks in the lineage.
    rank_name_dictionary: dict
        A dictionary where the keys are named ranks and the values are the names
        of the taxa that correspond to each of the named ranks in the lineage.
    agreement: float
        Level of agreement of the aggregated taxonomy.
    aggregated_taxa: list
        List of the aggregated taxonomic identifiers.

    Raises
    ------
    TaxidError
        If the input string is not a valid NCBI taxonomic identifier.
    """

    def __init__(
        self, taxid: int, taxdb: TaxDb, agreement: float, aggregated_taxa: List[int]
    ):
        super().__init__(taxid, taxdb)
        self.agreement = agreement
        self.aggregated_taxa = aggregated_taxa
