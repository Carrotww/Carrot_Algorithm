/* ************************************************************************** */
/*                                                                            */
/*                                                      :::    :::    :::     */
/*   Problem Number: 20006                             :+:    :+:      :+:    */
/*                                                    +:+    +:+        +:+   */
/*   By: rjgjfl <boj.kr/u/rjgjfl>                    +#+    +#+          +#+  */
/*                                                  +#+      +#+        +#+   */
/*   https://boj.kr/20006                          #+#        #+#      #+#    */
/*   Solved: 2025/09/09 21:08:09 by rjgjfl        ###          ###   ##.kr    */
/*                                                                            */
/* ************************************************************************** */

import java.util.*;
import java.io.*;

public class Main {

    static int P; // player cnt
    static int M; // max room
    static List<List<Player>> roomAry;

    static class Player {
        String nickName;
        int level;

        Player(String n, int l) {
            this.nickName = n;
            this.level = l;
        }
    }

    public static void main(String[] args) throws IOException {
        input();

        StringBuilder sb = new StringBuilder();

        // 출력하기
        for (List<Player> curRoom : roomAry) {
            if (curRoom.size() == M) {
                sb.append("Started!");
            } else {
                sb.append("Waiting!");
            }
            sb.append("\n");

            // 방에 있는 플레이어 정렬하기 -> 닉네임 사전 순으로 (중복 X)
            Comparator<Player> comparator = Comparator.comparing(p -> p.nickName);
            curRoom.sort(comparator);

            for (Player p : curRoom) {
                sb.append(p.level);
                sb.append(" ");
                sb.append(p.nickName);
                sb.append("\n");
            }
        }

        System.out.println(sb);
    }

    public static void input() throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        P = Integer.parseInt(st.nextToken());
        M = Integer.parseInt(st.nextToken());

        roomAry = new ArrayList<>();

        for (int i = 0; i < P; i++) {
            st = new StringTokenizer(br.readLine());
            int level = Integer.parseInt(st.nextToken());
            String nickName = st.nextToken();

            Player curPlayer = new Player(nickName, level);
            if (roomAry.isEmpty()) {
                // init
                roomAry.add(new ArrayList<>());
                roomAry.get(0).add(curPlayer);
            } else {
                boolean enterRoom = false;

                for (List<Player> room : roomAry) {
                    // 방이 꽉찬지 체크하기
                    int roomSize = room.size();
                    if (roomSize >= M) continue;

                    // 방에 들어갈 수 있는 레벨인지 체크하기
                    int deadLineLevel = room.get(0).level;
                    if (deadLineLevel + 10 < level || deadLineLevel - 10 > level) continue;

                    // 조건 만족하니까 방에 넣어주기
                    room.add(curPlayer);
                    enterRoom = true;
                    break;
                }

                // 들어간 방이 없다면 새 방 만들어서 넣어주기
                if (!enterRoom) {
                    List<Player> newRoom = new ArrayList<>();
                    newRoom.add(curPlayer);
                    roomAry.add(newRoom);
                }
            }
        }
    }
}