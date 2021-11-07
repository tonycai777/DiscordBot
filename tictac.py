from discord.ext import commands
import asyncio, random

class tictactoe(commands.Cog):
    # tic tac toe!

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(name="ttt")
    async def game(self, ctx: commands.Context):

        def vertical(board: list) -> str:
            x_pos = 0

            while x_pos < 3: # Checks each column position 0-2
                if board[0][x_pos] == board[1][x_pos] and\
                board[0][x_pos] == board[2][x_pos] and board[0][x_pos] != '- ':
                    return board[0][x_pos]
                else:
                    x_pos += 1

            return

        def horizontal(board: list) -> str:
            y_pos = 0

            while y_pos < 3: # Checks each row position 0-2
                if board[y_pos][0] == board[y_pos][1] and\
                board[y_pos][0] == board[y_pos][2] and board[y_pos][0] != '- ':
                    return board[y_pos][0]
                else:
                    y_pos += 1
                    
            return

        def diagonal(board: list) -> str:
            if board[0][0] == board[1][1] and\
                board[0][0] == board[2][2] and board[0][0] != '- ':
                    return board[0][0]
            if board[0][2] == board[1][1] and\
                    board[0][2] == board[2][0] and board[0][2] != '- ':
                    return board [0][2]
            else:
                return

        def find_winner(board: list) -> str:
            vertical_result = vertical(board)
            horizontal_result = horizontal(board)
            diagonal_result = diagonal(board)

            if vertical_result != None:
                return vertical_result
            elif horizontal_result != None:
                return horizontal_result
            elif diagonal_result != None:
                return diagonal_result
            else:
                return 'Draw'

        def print_board(board: list) -> str:
            message = '⠀a b c\n'
            count = 1
            for row in board:
                message = message + str(count) + ' '
                for column in row:
                    message = message + column
                message = message + "\n"
                count += 1
            return message

        board = [['- ', '- ', '-'], ['- ', '- ', '- '], ['- ', '- ', '- ']]
        correct_moves = ['a1', 'a2', 'a3', 'b1', 'b2', 'b3', 'c1', 'c2', 'c3']
        count = 0
        while count < 9:
            mesBoard = print_board(board)
            await ctx.send(mesBoard)
            message = await ctx.send('Enter position to play (ie. b2)')
            check = lambda m: m.author == ctx.author and m.channel == ctx.channel

            try:
                confirm = await self.bot.wait_for("message", check=check, timeout=30)
            except asyncio.TimeoutError:
                await message.edit(content="Game cancelled, timed out.")
                return

            if confirm.content in correct_moves:
                if confirm.content[0] == 'a':
                    current_move = [int(confirm.content[1]) - 1, 0]
                elif confirm.content[0] == 'b':
                    current_move = [int(confirm.content[1]) - 1, 1]
                elif confirm.content[0] == 'c':
                    current_move = [int(confirm.content[1]) - 1, 2]
            else:
                await ctx.send('Enter a correct position')
                continue

            if board[current_move[0]][current_move[1]] == 'X ' or\
                board[current_move[0]][current_move[1]] == 'O ':
                await ctx.send('Enter a non-empty position')
                continue
            else:
                board[current_move[0]][current_move[1]] = 'O '
                count += 1
            
            checkwin = find_winner(board)
            if checkwin != 'Draw':
                await ctx.send('You win!')
                mesBoard = print_board(board)
                await ctx.send(mesBoard)
                break
            else:
                compfirst_pos = random.randint(0, 2)
                compsec_pos = random.randint(0, 2)
                while board[compfirst_pos][compsec_pos] != '- ':
                    compfirst_pos = random.randint(0, 2)
                    compsec_pos = random.randint(0, 2)
                board[compfirst_pos][compsec_pos] = 'X '
                count += 1
                checkwin = find_winner(board)
                if checkwin != 'Draw':
                    await ctx.send('Computer wins!')
                    mesBoard = print_board(board)
                    await ctx.send(mesBoard)
                    break

        checkwin = find_winner(board)
        if checkwin == 'Draw':
            await ctx.send('Draw... :pensive:')
            mesBoard = print_board(board)
            await ctx.send(mesBoard)

def setup(bot: commands.Bot):
    bot.add_cog(tictactoe(bot))