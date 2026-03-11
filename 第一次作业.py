from typing import Iterable, Any
fruits:list[str]=["apple","banana","cherry","orange","mango"]
class DeleteItem:
    """
    插入列表元素
    """
    def __init__(self,iterable:Iterable[Any]):
        self.iterable = list(iterable)

    def delete(self,index_to_delete:int) -> None:
        """
        在列表中删除元素
        :param index_to_delete: 要删除元素的索引
        """
        #检验搜索合法性
        if index_to_delete < 0 or index_to_delete >= len(self.iterable):
            raise IndexError("索引超出列表范围")
        length_of_iterator:int = len(self.iterable)
        #从删除位置开始，将后面的元素依次向全覆盖
        for i in range(index_to_delete,length_of_iterator-1):
            self.iterable[i] = self.iterable[i+1]
        #删除最后一个空格
        self.iterable.pop()
delete_item=DeleteItem(fruits)
delete_item.delete(2)
print(delete_item.iterable)
