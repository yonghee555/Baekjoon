// 타임머신
// https://www.acmicpc.net/problem/11657

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    static class Bus {
        int end;
        int weight;

        Bus(int end, int weight) {
            this.end = end;
            this.weight = weight;
        }
    }
    static final int INF = 100000000;
    static int N, M;
    static long[] dist;
    static ArrayList<ArrayList<Bus>> graph;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");

        N = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        dist = new long[N + 1];
        Arrays.fill(dist, INF);

        graph = new ArrayList<>();
        for (int i = 0; i <= N; i++) {
            graph.add(new ArrayList<>());
        }
        for (int i = 0; i < M; i++) {
            st = new StringTokenizer(br.readLine(), " ");
            int A = Integer.parseInt(st.nextToken());
            int B = Integer.parseInt(st.nextToken());
            int C = Integer.parseInt(st.nextToken());
            graph.get(A).add(new Bus(B, C));
        }

        // 반환값이 true인 경우 음수 사이클이 존재
        if (BellmanFord())
            System.out.println(-1);
        else {
            for (int i = 2; i <= N; i++) {
                if (dist[i] == INF)
                    System.out.println(-1);
                else
                    System.out.println(dist[i]);
            }
        }
    }

    public static boolean BellmanFord() {
        // 첫 번째 노드 거리 0으로 초기화
        dist[1] = 0;
        for (int i = 1; i < N; i++) {
            for (int j = 1; j <= N; j++) {
                for (Bus bus : graph.get(j)) {
                    if (dist[j] == INF)
                        break;
                    if (dist[bus.end] > dist[j] + bus.weight) {
                        dist[bus.end] = dist[j] + bus.weight;
                    }
                }
            }
        }
        // N - 1번 수행 후 N번 째에 거리가 갱신되는 경우가 있다면 음수 사이클이 존재
        for (int i = 1; i <= N; i++) {
            for (Bus bus : graph.get(i)) {
                if (dist[i] == INF)
                    break;
                if (dist[bus.end] > dist[i] + bus.weight)
                    return true;
            }
        }
        return false;
    }
}
