class HTMLNode:

    def __init__(self, tag=None, value=None, children=None, props=None):

        self.tag = tag
        self.value = value
        self.children = children if children is not None else []
        self.props = props if props is not None else {}

    
    def to_html(self):
        raise NotImplemented("Child classes will override this method to render themselves as HTML.")
    
    def props_to_html(self):

        return "".join(f' {k}="{v}"' for k, v in self.props.items())
    

    def __repr__(self) -> str:
        return f"HTMLNode (tag={self.tag}, value= {self.value}, children= {self.children}, props={self.props})"
    
class LeafNode(HTMLNode):

    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
            if self.value is None:
                raise ValueError("No value")
            if self.tag is None:
                return self.value
            return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
        
    def __repr__(self) -> str:
            return f"LeafNode({self.tag}, {self.value}, {self.props})"
    
