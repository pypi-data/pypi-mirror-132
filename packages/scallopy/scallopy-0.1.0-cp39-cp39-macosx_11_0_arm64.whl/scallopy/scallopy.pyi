from typing import List, Union, Tuple, Optional, Any

from .provenance import ScallopProvenance
from .io import CSVFileOptions

class InternalScallopContext:
  def __init__(
    self,
    provenance: str = "unit",
    k: int = 3,
    custom_provenance: Optional[ScallopProvenance] = None,
  ) -> None: ...

  def clone(self) -> InternalScallopContext: ...

  def set_k(self, k: int): ...

  def run(self) -> None: ...

  def add_relation(
    self,
    relation: str,
    load_csv: Optional[Union[CSVFileOptions, str]] = None,
  ) -> None: ...

  def add_facts(self, relation: str, elems: List[Tuple]) -> None: ...

  def add_rule(
    self,
    rule: str,
    tag: Optional[Any] = None,
  ) -> None: ...

  def dump_front_ir(self): ...

  def relation(self, relation: str) -> InternalScallopCollection: ...

  def relation_is_computed(self, relation: str) -> bool: ...

  def num_relations(self, include_hidden: bool = False) -> int: ...

  def relations(self, include_hidden: bool = False) -> List[str]: ...


class InternalScallopCollection:
  """
  A collection of tuples (maybe associated with tags)
  """
  def num_input_facts(self) -> Optional[int]:
    """
    Get the number of input facts for a valid provenance semiring
    """

  def __iter__(self) -> InternalScallopCollectionIterator:
    """
    Iterate through the tuples of the collection
    """


class InternalScallopCollectionIterator:
  """
  An iterator over the scallop collection
  """

  def __next__(self) -> Tuple:
    """
    Get the next tuple in the collection
    """
