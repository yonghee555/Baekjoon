// 잃어버린 괄호
// https://www.acmicpc.net/problem/1541

import java.io.IOException;
import java.util.Scanner;

class Main {
    public static void main(String[] args) throws IOException {
        int answer = 0;
        Scanner sc = new Scanner(System.in);
        String[] sick = sc.nextLine().split("-");
        sc.close();

        String[] first = sick[0].split("\\+");
        for (int j = 0; j < first.length; j++) {
            answer += Integer.parseInt(first[j]);
        }

        for (int i = 1; i < sick.length; i++) {
            String[] b = sick[i].split("\\+");
            for (int j = 0; j < b.length; j++) {
                answer -= Integer.parseInt(b[j]);
            }
        }
        System.out.println(answer);
        return;
    }
}
