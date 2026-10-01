class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        position_dict = {}
        check_list= []
        box_list = []
        check_list_x = []
        check_list_y = []

        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    position_dict[(i,j)] = board[i][j]

        for i in range(1,10,1):
            for key, value in position_dict.items():
                if int(value) == i:
                    check_list.append(key)
                    check_list_x.append(key[0])
                    check_list_y.append(key[1])
            
            check_set_x = set(check_list_x)
            if len(check_list_x) != len(check_set_x):
                return False

            check_set_y = set(check_list_y)
            if len(check_list_y) != len(check_set_y):
                return False

            for coor in check_list:
                if coor[0] < 3:
                    if coor[1] < 3:
                        box_list.append((0,0))
                    elif coor[1] < 6:
                        box_list.append((0,1))
                    elif coor[1] < 9:
                        box_list.append((0,2))
                elif coor[0] < 6:
                    if coor[1] < 3:
                        box_list.append((1,0))
                    elif coor[1] < 6:
                        box_list.append((1,1))
                    elif coor[1] < 9:
                        box_list.append((1,2))
                elif coor[0] < 9:
                    if coor[1] < 3:
                        box_list.append((2,0))
                    elif coor[1] < 6:
                        box_list.append((2,1))
                    elif coor[1] < 9:
                        box_list.append((2,2))

            box_set = set(box_list)
            if len(box_list) != len(box_set):
                return False
                
            box_list.clear()
            check_list.clear()
            check_list_x.clear()
            check_list_y.clear()

        return True