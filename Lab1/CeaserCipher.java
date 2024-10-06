public class CaesarCipher {
    public static String cipher(String message, int offset) {
        String result = "";
        for (char ch : message.toCharArray()) {
            if (Character.isLetter(ch) && Character.isLowerCase(ch)) {
                char base = 'a';
                result = result + ((char) ((ch - base + offset) % 26 + base));
            } else {
                result = result + (ch);
            }
        }
        return result.toUpperCase().toString();
    }

    public static void main(String[] args) {
        String plaintext = "hello, world!";
        int k = 3;
        String encrypted = cipher(plaintext, k);
        System.out.println("Plain Text: " + plaintext);
        System.out.println("Cipher Text: " + encrypted);
    }
}
