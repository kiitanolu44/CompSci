data = dict(
    foo = None,
    bar = 1,
    bla = [1,2,3],
    bla_bla = dict(
        bla_bla_bla = None,
        bla_bla_bla_bla = [
            dict(
                hello="goodbye"
            ),
            dict(
                yes="no"
            )
        ]
    )
)

def traverse_tree(node, depth) -> None:
    if (
        node is None
    ) or isinstance(
        node,str
    ) or isinstance(
        node,float
    ) or isinstance(
        node,int
    ):
        return [(node,depth)]
    
    if isinstance(node,dict):
        children = node.values()
    if isinstance(node,list) or isinstance(node,tuple):
        children = node

    result = []
    for child in children:
        result.extend(traverse_tree(node=child, depth = depth + 1))
    return result
            
x= traverse_tree(node=data, depth=0)
print(x)
