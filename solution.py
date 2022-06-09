"""
Barebone code created by: Tuan-Phong Nguyen
Date: 2022-06-03
"""

import logging
from typing import Dict, List, Tuple

logger = logging.getLogger(__name__)


def your_solution(animal: str, doc_list: List[Dict[str, str]]) -> List[Tuple[str, int]]:
    """
    Task: Extract things that the given animal eats. These things should be mentioned in the given list of documents.
    Each document in ``doc_list`` is a dictionary with keys ``animal``, ``url``, ``title`` and ``text``, whereas
    ``text`` points to the content of the document.

    :param animal: The animal to extract diets for.
    :param doc_list: A list of retrived documents.
    :return: A list of things that the animal eats along with their frequencies.
    """

    logger.info(f"Animal: \"{animal}\". Number of documents: {len(doc_list)}.")

    # You can directly use the following list of documents, which is a list of str, if you don't need other information (i.e., url, title).
    documents = [doc["text"] for doc in doc_list]

    # TODO Implement your own method here
    # You must extract things that are explicitly mentioned in the documents.
    # You cannot use any external CSK resources (e.g., ConceptNet, Quasimodo, Ascent, etc.).

    # Output example:
    return [("grass", 10), ("fish", 3)]
