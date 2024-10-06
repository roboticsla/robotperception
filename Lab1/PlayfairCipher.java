import java.util.Scanner;

public class PlayfairCipher {

    String key;
    char[][] matrix;

    public PlayfairCipher(String key) {
        setKey(key);
    }

    void setKey(String key) {

        key = key.toUpperCase();
        key = key.replace("J", "I");
        boolean[] used = new boolean[26]; // to keep track of used letters
        StringBuilder cleanedKey = new StringBuilder();

        for (char c : key.toCharArray()) {
            if (!used[c - 'A']) {
                cleanedKey.append(c);
                used[c - 'A'] = true;
            }
        }

        for (char c = 'A'; c <= 'Z'; c++) {
            if (c != 'J' && !used[c - 'A']) {
                cleanedKey.append(c);
            }
        }

        this.key = cleanedKey.toString();
        generateMatrix();
    }

    void generateMatrix() {
        matrix = new char[5][5];
        int index = 0;
        for (int i = 0; i < 5; i++) {
            for (int j = 0; j < 5; j++) {
                matrix[i][j] = key.charAt(index);
                index++;
            }
        }
    }

    String preprocess(String plaintext) {
        plaintext = plaintext.toUpperCase();
        plaintext = plaintext.replace("J", "I");

        StringBuilder processedText = new StringBuilder(plaintext);
        for (int i = 0; i < processedText.length() - 1; i += 2) {
            if (processedText.charAt(i) == processedText.charAt(i + 1)) {
                processedText.insert(i + 1, 'X');
            }
        }

        if (processedText.length() % 2 != 0) {
            processedText.append('X');
        }

        return processedText.toString();
    }

    String encodeDigraph(char a, char b) {
        int r1 = -1, r2 = -1, c1 = -1, c2 = -1;
        for (int i = 0; i < 5; i++) {
            for (int j = 0; j < 5; j++) {
                if (matrix[i][j] == a) {
                    r1 = i;
                    c1 = j;
                } else if (matrix[i][j] == b) {
                    r2 = i;
                    c2 = j;
                }
            }
        }

        if (r1 == r2) {
            c1 = (c1 + 1) % 5;
            c2 = (c2 + 1) % 5;
        } else if (c1 == c2) {
            r1 = (r1 + 1) % 5;
            r2 = (r2 + 1) % 5;
        } else {
            int temp = c1;
            c1 = c2;
            c2 = temp;
        }

        return "" + matrix[r1][c1] + matrix[r2][c2];
    }

    public String encrypt(String plaintext) {
        plaintext = preprocess(plaintext);

        StringBuilder ciphertext = new StringBuilder();

        for (int i = 0; i < plaintext.length(); i += 2) {
            char a = plaintext.charAt(i);
            char b = plaintext.charAt(i + 1);
            ciphertext.append(encodeDigraph(a, b));
        }

        return ciphertext.toString();
    }

    public static void main(String[] args) {
        PlayfairCipher cipher = new PlayfairCipher("VIRATKOHLI");
        Scanner sc = new Scanner(System.in);

        String plaintext = sc.nextLine();
        String encrypted = cipher.encrypt(plaintext);

        System.out.println("Plaintext: " + plaintext);
        System.out.println("Encrypted: " + encrypted);
        sc.close();
    }
}
