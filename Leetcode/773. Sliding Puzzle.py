class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        s = ''.join(str(d) for row in board for d in row)
        dq = collections.deque()
        seen = {s}
        dq.append((s, s.index('0')))

        steps, height = 0, len(board)
        width = len(board[0])

        # Directions to move (row_delta, col_delta)
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        while dq:
            for _ in range(len(dq)):
                t, i = dq.popleft()
                if t == '123450':
                    return steps
                # Convert the 1D index back to 2D (row, col)
                x, y = divmod(i, width)
                for r_delta, c_delta in directions:
                    r, c = x + r_delta, y + c_delta
                    if 0 <= r < height and 0 <= c < width:
                        # Calculate the new 1D index
                        new_i = r * width + c
                        ch = list(t)
                        # Swap '0' with the target position
                        ch[i], ch[new_i] = ch[new_i], ch[i]
                        s = ''.join(ch)
                        if s not in seen:
                            seen.add(s)
                            dq.append((s, new_i))
            steps += 1
        return -1
