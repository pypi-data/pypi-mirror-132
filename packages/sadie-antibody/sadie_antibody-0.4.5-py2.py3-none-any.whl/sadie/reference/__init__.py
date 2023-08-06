__version__ = "0.4.5"
from sadie.reference.reference import Reference
from sadie.reference.internal_data import make_internal_annotaion_file
from sadie.reference.igblast_ref import make_igblast_ref_database
from sadie.reference.aux_file import make_auxillary_file
from pathlib import Path
import logging

logger = logging.getLogger("reference")


def make_germline_database(reference: Reference, output_path: Path) -> Path:
    """
    Make the igblast database in an output path from the reference object

    Parameters
    ----------
    reference : Reference
        The reference object
    output_path : Path
        A path to dump the igblast reference structure

    Returns
    -------
    Path
        On success return path of dumped database file
    """ """
    Make the igblast database in an output path from the reference object

    Parameters
    ----------
    reference : Reference
        The reference object
    output_path : Path
        A path to dump the igblast reference structure

    Returns
    -------
    Path
        On success return path of dumped database file
    """
    make_internal_annotaion_file(reference, output_path)
    logger.info(f"Generated Internal Data {output_path}/internal_data")
    make_igblast_ref_database(reference, output_path)
    logger.info(f"Generated Blast Data {output_path}/blast")
    make_auxillary_file(reference, output_path)
    logger.info(f"Generated Aux Data {output_path}/aux_db")
    return output_path


__all__ = ["Reference"]
