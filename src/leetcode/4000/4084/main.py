class Solution:
    def findColoredRoot(self, edges: list[list[int]], colors: str) -> int:
        circle_dir = {'R': 'B', 'B': 'W', 'W': 'R'}
        
        edge_dict = {i: {'from': [], 'to': []} for i in range(len(colors))}
        for i in range(len(edges)):
            x = edges[i][0]
            x_color = colors[x]
            y = edges[i][1]
            y_color = colors[y]
            if circle_dir[x_color] == y_color:
                edge_dict[x]['to'].append(y)
                edge_dict[y]['from'].append(x)
            elif circle_dir[y_color] == x_color:
                edge_dict[y]['to'].append(x)
                edge_dict[x]['from'].append(y)
            else:
                return -1

        ans = -1
        for i in range(len(colors)):
            edge_inf = edge_dict[i]
            if len(edge_inf['from']) == 0:
                if ans != -1:
                    return -1
                ans = i
            elif len(edge_inf['from']) >= 2:
                return -1
            if len(edge_inf['to']) >= 3:
                return -1
        return ans
    