class Solution:
    def SimplifyPath(self, path: str) -> str:
        stack=[]
        path=path.split('/')
        for i in path:
            if stack and i == "..":
                stack.pop()
            elif i not in [".","..",""]:
                stack.append(i)
        return "/" + "/".join(stack)
    
s=Solution()
simplified_path = s.SimplifyPath("/.../a/../b/c/../d/./")
print("Simplified path: ",simplified_path)
'''
i/p: "/home/"  o/p: "/home"
i/p: "/home//foo/"  o/p: "/home/foo"
i/p: "/../"  o/p: "/home/foo"

i/p: "/.../a/../b/c/../d/./"  o/p: "/.../b/d"
'''