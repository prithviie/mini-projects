import java.util.*;

public class TicTacToe {

    private static char[] board = {' ',' ',' ',' ',' ',' ',' ',' ',' ',' '};

    public static void printBoard(char[] board){
        System.out.println(" " + board[1] + " | " + board[2] + " | " + board[3]);
        System.out.println("---|---|---");
        System.out.println(" " + board[4] + " | " + board[5] + " | " + board[6]);
        System.out.println("---|---|---");
        System.out.println(" " + board[7] + " | " + board[8] + " | " + board[9]);
    }

    public static void insertMove(char letter, int pos){
        board[pos] = letter;
    }

    public static boolean isAvailable(int pos){
        return board[pos] == ' ';
    }

    public static boolean isWinner(char[] board, char le){

        return (board[1] == le && board[2] == le && board[3] == le) ||
                (board[4] == le && board[5] == le && board[6] == le) ||
                (board[7] == le && board[8] == le && board[9] == le) ||
                (board[1] == le && board[4] == le && board[7] == le) ||
                (board[2] == le && board[5] == le && board[8] == le) ||
                (board[3] == le && board[6] == le && board[9] == le) ||
                (board[1] == le && board[5] == le && board[9] == le) ||
                (board[3] == le && board[5] == le && board[7] == le);
    }

    public static boolean isBoardFull(char[] board){
        int count = 0;
        for (char c: board) {
            if (c == ' '){
                count++;
            }
        }
        if (count>=1){
            return false;
        }
        else{
            return true;
        }
    }

    public static void playerMove(){
        boolean run = true;
        while (run){
            Scanner scanner = new Scanner(System.in);
            System.out.print("Enter position to place x (1-9): ");
            try{
                int move = scanner.nextInt();
                if(move>0 && move<10){
                    if(isAvailable(move)){
                        insertMove('x', move);
                        run = false;
                    }
                    else{
                        System.out.println("Position already occupied");
                    }
                }
                else{
                    System.out.println("Enter between 1-9");
                }
            }
            catch(Exception e){
                System.out.println("Enter a number!");
            }
        }
    }

    private static boolean contains(int[] array, int num){
        for(int n: array){
            if(n == num){
                return true;
            }
        }
        return false;
    }

    public static int selectRandom(ArrayList<Integer> array){
        Random r = new Random();
        return array.get(r.nextInt(array.size()));
    }

    public static int compMove(){

        int move = 0;

        ArrayList<Integer> possibleMoves = new ArrayList<Integer>();
        for(int i=1; i<board.length; i++){
            if (board[i] == ' '){
                possibleMoves.add(i);
            }
        }

        char[] players = {'o', 'x'};
        for(char letter: players){
            for(Integer m : possibleMoves){

                char[] boardCopy = new char[board.length];
                for(int i=1; i<board.length; i++){
                    boardCopy[i] = board[i];
                }

                boardCopy[m] = letter;

                if(isWinner(boardCopy, letter)){
                    move = m;
                    return move;
                }
            }
        }

        ArrayList<Integer> cornersOpen = new ArrayList<Integer>();
        int[] corners = new int[]{1,3,5,7};

        for(int i : possibleMoves){
            if (contains(corners, i)){
                cornersOpen.add(i);
            }
        }

        if (cornersOpen.size() > 0){
            move = selectRandom(cornersOpen);
            return move;
        }

        if (possibleMoves.contains(5)){
            move = 5;
            return move;
        }

        ArrayList<Integer> edgesOpen = new ArrayList<Integer>();
        int[] edges = new int[]{2,4,6,8};

        for(int i : possibleMoves){
            if (contains(edges, i)){
                edgesOpen.add(i);
            }
        }

        if (edgesOpen.size() > 0){
            move = selectRandom(edgesOpen);
        }

        return move;
    }

    public static void main(String[] args){
        System.out.println("Welcome to Tic Tac Toe!");
        printBoard(board);

        while (!isBoardFull(board)){

            if (!isWinner(board,'o')){
                playerMove();
                // printBoard(board);
            }
            else{
                System.out.println("Computer won!");
                break;
            }

            if(!isWinner(board, 'x')){
                int move = compMove();
                if (move == 0){
                    System.out.println("Tie");
                    break;
                }
                else{
                    insertMove('o', move);
                    System.out.println("Computer placed o at " + move);
                    printBoard(board);
                }
            }

            else{
                System.out.println("You won!");
                break;
            }
        }

        if(isBoardFull(board)){
            System.out.println("Tie");
        }
    }

}
