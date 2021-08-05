// 단지번호붙이기
// https://www.acmicpc.net/problem/2667

import java.io.IOException;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Scanner;

class no_2667 {
    static int n;
    static int[][] map;
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);

        n = sc.nextInt();
        map = new int[n][n];

        for (int i = 0; i < n; i++) {
            String input = sc.next();
            for (int j = 0; j < n; j++) {
                map[i][j] = input.charAt(j) - '0';
            }
        }
        sc.close();

        ArrayList<Integer> answer = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                int m = dfs(i, j);
                if (m > 0)
                    answer.add(m);
            }
        }
        Collections.sort(answer);
        System.out.println(answer.size());
        for (int i : answer) System.out.println(i);
    }

    public static int dfs(int x, int y) {
        if (x < 0 || y < 0 || x >= n || y >= n)
            return 0;
        if (map[x][y] == 1) {
            map[x][y] = 0;
            return 1 + dfs(x + 1, y) + dfs(x, y + 1) + dfs(x - 1, y) + dfs(x, y - 1);
        }
        return 0;
    }
}
