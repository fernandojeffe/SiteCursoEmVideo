/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package calculo1;
import java.util.Scanner;

/**
 *
 * @author fernando
 */
public class Calculo1 {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
        Scanner input = new Scanner(System.in);
        
        int num1;
        int num2;
        int soma;
        
        System.out.print("Digite um numero: ");
        num1 = input.nextInt();
        System.out.print("Digite o segundo numero: ");
        num2 = input.nextInt();
        
        soma = num1+num2;
        System.out.printf("A soma e %d%n", soma);    
        
        
    }
    
}
