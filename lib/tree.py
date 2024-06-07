class Tree:
  def __init__(self, root = None):
    self.root = root

  def get_element_by_id(self, id):
    nodes_to_traverse= [self.root]

    while nodes_to_traverse:
      node = nodes_to_traverse.pop()
      if node['id'] == id:
        return node
      if node['children']:
       
        nodes_to_traverse.extend(node['children'])

    return None
