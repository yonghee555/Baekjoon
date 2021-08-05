// 바이러스
// https://www.acmicpc.net/problem/2606

import java.io.IOException;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

class no_2606 {
    static int[][] graph;
    static boolean[] visited;
    static int n;
    static int m;
    static int count = 0;
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        m = sc.nextInt();

        graph = new int[n + 1][n + 1];
        visited = new boolean[n + 1];

        for (int i = 0; i < m; i++) {
            int x = sc.nextInt();
            int y = sc.nextInt();
            graph[x][y] = graph[y][x] = 1;
        }
        sc.close();
        bfs();
        System.out.println(count);
    }

    public static void dfs(int i) {
        visited[i] = true;
        for (int j = 1; j <= n; j++) {
            if (graph[i][j] == 1 && visited[j] == false) {
                count++;
                dfs(j);
            }
        }
    }

    public static void bfs() {
        visited[1] = true;
        Queue<Integer> queue = new LinkedList<>();
        queue.offer(1);
        while (!queue.isEmpty()) {
            int i = queue.poll();
            for (int j = 0; j <= n; j++) {
                if (graph[i][j] == 1 && visited[j] == false) {
                    count++;
                    queue.offer(j);
                    visited[j] = true;
                }
            }
        }
    }
}
