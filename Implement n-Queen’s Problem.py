class NQueens:
    def __init__(self, n):
        self.n = n
        self.board = [[0 for x in range(n)] for y in range(n)]
        self.solutions = []

    def solve(self):
        self.solve_helper(0)

    def solve_helper(self, col):
        if col == self.n:
            # Found a solution
            solution = []
            for row in range(self.n):
                solution.append("".join(["Q" if self.board[row][col] == 1 else "." for col in range(self.n)]))
            self.solutions.append(solution)
            return True
        else:
            for row in range(self.n):
                if self.is_valid_move(row, col):
                    self.board[row][col] = 1
                    self.solve_helper(col + 1)
                    self.board[row][col] = 0

    def is_valid_move(self, row, col):
        # Check row
        for i in range(col):
            if self.board[row][i] == 1:
                return False

        # Check upper diagonal
        i = row
        j = col
        while i >= 0 and j >= 0:
            if self.board[i][j] == 1:
                return False
            i -= 1
            j -= 1

        # Check lower diagonal
        i = row
        j = col
        while i < self.n and j >= 0:
            if self.board[i][j] == 1:
                return False
            i += 1
            j -= 1

        return True
nq = NQueens(4)
nq.solve()
print(nq.solutions)  # Output: [['.Q..', '...Q', 'Q...', '..Q.'], ['..Q.', 'Q...', '...Q', '.Q..']]
