class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for r in range(9):
            seen = set()
            for c in range(9):
                val = board[r][c]
                # skip "." and check/add val
                if val == ".":
                    continue
                if val in seen:
                    return False
                seen.add(val)

        for c in range(9):
            seen = set()
            for r in range(9):
                val = board[r][c]
                # skip "." and check/add val
                if val == ".":
                    continue
                if val in seen:
                    return False
                seen.add(val)

        for box_r in range(3):
            for box_c in range(3):
                seen = set()
                for r in range(box_r * 3, box_r * 3 + 3):
                    for c in range(box_c * 3, box_c * 3 + 3):
                        val = board[r][c]
                        if val == ".":
                            continue
                        if val in seen:
                            return False
                        seen.add(val)
        return True