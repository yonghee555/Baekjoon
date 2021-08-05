// DFS와 BFS
// https://www.acmicpc.net/problem/1260

import java.io.IOException;
import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

class no_1260 {
    static int[][] graph;
    static boolean[] visited;
    static int n;
    static int m;
    static int v;

    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        m = sc.nextInt();
        v = sc.nextInt();

        graph = new int[n + 1][n + 1];
        visited = new boolean[n + 1];

        for (int i = 0; i < m; i++) {
            int x = sc.nextInt();
            int y = sc.nextInt();
            graph[x][y] = graph[y][x] = 1;
        }

        sc.close();
        dfs(v);
        System.out.println();
        visited = new boolean[n + 1];
        bfs();
    }

    public static void dfs(int i) {
        visited[i] = true;
        System.out.print(i + " ");

        for (int j = 1; j <= n; j++) {
            if (graph[i][j] == 1 && visited[j] == false)
                dfs(j);
        }
    }

    public static void bfs() {
        Queue<Integer> queue = new LinkedList<Integer>();
        queue.offer(v);
        visited[v] = true;
        System.out.print(v + " ");
        while (queue.isEmpty() == false) {
            int i = queue.poll();

            for (int j = 1; j <= n; j++) {
                if (graph[i][j] == 1 && visited[j] == false) {
                    queue.offer(j);
                    visited[j] = true;
                    System.out.print(j + " ");
                }
            }
        }
    }
}