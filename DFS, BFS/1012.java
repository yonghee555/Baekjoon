// 유기농 배추
// https://www.acmicpc.net/problem/1012

import java.io.IOException;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

class no_1012 {
    static int m;
    static int n;
    static int[][] graph;

    static int[] dx = {-1, 1, 0, 0};
    static int[] dy = {0, 0, -1, 1};
    public static void main (String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        for (int i = 0; i < t; i++) {
            m = sc.nextInt();
            n = sc.nextInt();
            int k = sc.nextInt();

            graph = new int[n][m];

            for (int j = 0; j < k; j++) {
                int x = sc.nextInt();
                int y = sc.nextInt();
                graph[y][x] = 1;
            }
            int count = 0;
            for (int a = 0; a < n; a++) {
                for (int b = 0; b < m; b++) {
                    if (graph[a][b] == 1) {
                        bfs(a, b);
                        count++;
                    }
                }
            }
            System.out.println(count);
        }
        sc.close();
    }

    public static void dfs(int x, int y) {
        if (x < 0 || y < 0 || x >= n || y >= m)
            return;
        if (graph[x][y] == 1) {
            graph[x][y] = 0;
            dfs(x + 1, y);
            dfs(x, y + 1);
            dfs(x - 1, y);
            dfs(x, y - 1);
        }
        return;
    }

    public static void bfs(int x, int y) {
        Queue<int[]> queue = new LinkedList<>();
        queue.offer(new int[] {x, y});
        while (!queue.isEmpty()) {
            x = queue.peek()[0];
            y = queue.peek()[1];
            queue.poll();
            graph[x][y] = 0;
            for (int i = 0; i < 4; i++) {
                int nx = x + dx[i];
                int ny = y + dy[i];
                if (nx >= 0 && ny >= 0 && nx < n && ny < m) {
                    if (graph[nx][ny] == 1) {
                        queue.offer(new int[] {nx, ny});
                        graph[nx][ny] = 0;
                    }
                }
            }
        }
    }
}
