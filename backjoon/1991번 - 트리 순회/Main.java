/* ************************************************************************** */
/*                                                                            */
/*                                                      :::    :::    :::     */
/*   Problem Number: 1991                              :+:    :+:      :+:    */
/*                                                    +:+    +:+        +:+   */
/*   By: rjgjfl <boj.kr/u/rjgjfl>                    +#+    +#+          +#+  */
/*                                                  +#+      +#+        +#+   */
/*   https://boj.kr/1991                           #+#        #+#      #+#    */
/*   Solved: 2025/10/14 14:08:48 by rjgjfl        ###          ###   ##.kr    */
/*                                                                            */
/* ************************************************************************** */

import java.util.*;
import java.io.*;

public class Main {
    static StringBuilder sb = new StringBuilder();

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());

        Node[] ary = new Node[N + 1];

        for (int i = 0; i < N; i++) {
            String line = br.readLine().replace(" ", "");
            char val = line.charAt(0);
            char left = line.charAt(1);
            char right = line.charAt(2);

            if (ary[val - 'A'] == null) {
                ary[val - 'A'] = new Node(val);
            }

            if (left != '.') {
                ary[left - 'A'] = new Node(left);
                ary[val - 'A'].setLeftNode(ary[left - 'A']);
            }

            if (right != '.') {
                ary[right - 'A'] = new Node(right);
                ary[val - 'A'].setRightNode(ary[right - 'A']);
            }
        }

        preOrder(ary[0]);
        sb.append('\n');
        inOrder(ary[0]);
        sb.append('\n');
        postOrder(ary[0]);

        System.out.println(sb);

        // ABDCEFG
        // DBAECFG
        // DBEGFCA
    }

    static void preOrder(Node node) {
        if (node == null) return;
        sb.append(node.val);
        preOrder(node.left);
        preOrder(node.right);
    }

    // 중위순회
    static void inOrder(Node node) {
        if (node == null) return;
        inOrder(node.left);
        sb.append(node.val);
        inOrder(node.right);

    }

    // 후위순회
    static void postOrder(Node node) {
        if (node == null) return;
        postOrder(node.left);
        postOrder(node.right);
        sb.append(node.val);
    }

    // root -> left -> right
    static void preOrderIter(Node root) {
        if (root == null) return;

        Deque<Node> d = new ArrayDeque<>();
        d.push(root);

        while (!d.isEmpty()) {
            Node cur = d.pop();
            sb.append(cur.val);
            if (cur.right != null) d.push(cur.right);
            if (cur.left != null) d.push(cur.left);
        }
    }

    // left -> root -> right
    static void inOrderIter(Node root) {
        Deque<Node> d = new ArrayDeque<>();
        Node cur = root;

        while (!d.isEmpty() || cur != null) {
            while (cur != null) {
                d.push(cur);
                cur = cur.left;
            }

            cur = d.pop();
            sb.append(cur.val);
            cur = cur.right;
        }
    }

    // left -> right -> root
    static void postOrderIter(Node root) {
        Deque<Node> d = new ArrayDeque<>();
        Node cur = root;
        Node last = null;

        while (!d.isEmpty() || cur != null) {
            if (cur != null) {
                d.push(cur);
                cur = cur.left;
            } else {
                Node peek = d.peek();
                if (peek.right != null && peek.right != last) {
                    cur = peek.right;
                } else {
                    sb.append(peek.val);
                    last = d.pop();
                }
            }
        }
    }

    static void postOrderIter2(Node root) {
        Stack<Node> stack = new Stack<>();
        Node cur = root;
        Node last = null;

        while (!stack.isEmpty() || cur != null) {
            if (cur != null) {
                cur = cur.left;
                stack.push(cur);
            } else {
                Node peek = stack.peek();

                // 오른쪽 있으면 가주고 && 마지막 나온 값이랑 달라야함
                if (peek.right != null && peek.right != last) {
                    cur = peek.right;
                    // 이미 들어간 값 넣어주고 last 갱신
                } else {
                    sb.append(peek.val);
                    last = stack.pop();
                }
            }
        }
    }

    static class Node {
        char val;
        Node left;
        Node right;

        Node(char val) {
            this.val = val;
            this.left = null;
            this.right = null;
        }

        void setLeftNode(Node node) {
            this.left = node;
        }

        void setRightNode(Node node) {
            this.right = node;
        }
    }
}