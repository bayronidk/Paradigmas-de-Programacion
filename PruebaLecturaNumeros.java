import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.Reader;

class LecturaNumeros extends BufferedReader {
    
    // Constructores
    public LecturaNumeros() {
        super(new InputStreamReader(System.in));
    }

    public LecturaNumeros(Reader r) {
        super(r);
    }

    // Métodos para leer números enteros
    public int readInt() throws IOException {
        return Integer.parseInt(this.readLine());
    }

    public int readInt(String mensaje) throws IOException {
        System.out.print(mensaje);
        return this.readInt();
    }

    public Integer readInteger() throws IOException {
        return this.readInt();
    }

    public Integer readInteger(String mensaje) throws IOException {
        System.out.print(mensaje);
        return this.readInt();
    }

    // Métodos para leer números de punto flotante
    public double readDouble() throws IOException {
        return Double.parseDouble(this.readLine());
    }

    public double readDouble(String mensaje) throws IOException {
        System.out.print(mensaje);
        return this.readDouble();
    }
}

public class PruebaLecturaNumeros {
    public static void main(String[] args) {
        try {
            LecturaNumeros lector = new LecturaNumeros();
            
            System.out.println("Introduce 2 números enteros, 1 número entero (en forma de objeto Integer), 1 número decimal y 1 número decimal (en forma de objeto Double):");

            int entero1 = lector.readInt("Introduce un número entero: ");
            int entero2 = lector.readInt("Introduce otro número entero: ");
            Integer integer = lector.readInteger("Introduce un número entero (como Integer): ");
            double decimal1 = lector.readDouble("Introduce un número decimal: ");
            Double decimal2 = lector.readDouble("Introduce otro número decimal (como Double): ");

            System.out.println("Los números introducidos son:");
            System.out.println("Entero 1: " + entero1);
            System.out.println("Entero 2: " + entero2);
            System.out.println("Integer: " + integer);
            System.out.println("Decimal 1: " + decimal1);
            System.out.println("Decimal 2: " + decimal2);

            lector.close();
        } catch (IOException e) {
            System.err.println("Error al leer la entrada.");
            e.printStackTrace();
        }
    }
}
