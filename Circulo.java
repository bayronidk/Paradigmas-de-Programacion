public class Circulo {
    private String color;
    private double radio;

    public Circulo(String color, double radio) {
        this.color = color;
        this.radio = radio;
    }

    public double getArea() {
        return area();
    }

    public double getPerimetro() {
        return perimetro();
    }

    public String getColor() {
        return color;
    }

    private double area() {
        return Math.PI * Math.pow(radio, 2);
    }

    private double perimetro() {
        return 2 * Math.PI * radio;
    }
        public static void main(String[] args) {
            Circulo circulo = new Circulo("rojo", 5.0);
            System.out.println("Color del círculo: " + circulo.getColor());
            System.out.println("Área del círculo: " + circulo.getArea());
            System.out.println("Perímetro del círculo: " + circulo.getPerimetro());
        }
    
}

