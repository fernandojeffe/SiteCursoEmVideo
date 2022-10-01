/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Project/Maven2/JavaApp/src/main/java/${packagePath}/${mainClassName}.java to edit this template
 */

package com.mycompany.operadordeiguadade;

import java.util.Scanner;

/**
 *
 * @author fernando
 */
public class OperadorDeIguadade {

    public static void main(String[] args) {
       // Cria o metodo para entrada de daodos no terminal// 
        Scanner input = new Scanner(System.in);
        
        int num1;
        int num2;
        
        System.out.print("Digite o primeiro numero: ");
        num1 = input.nextInt();
        
        System.out.print("Digite o segundo numero: ");
        num2 = input.nextInt(); 
        
        if (num1 == num2)
            System.out.printf("%d == %d%n",num1, num2);
        if (num1 != num2)
            System.out.printf("%d != %d%n",num1, num2);
        if (num1 < num2)
            System.out.printf("%d < %d%n",num1, num2);
        if (num1 > num2)
            System.out.printf("%d > %d%n",num1, num2);
        if (num1 >= num2)
            System.out.printf("%d >= %d%n",num1, num2);
        if (num1 <= num2)
            System.out.printf("%d <= %d%n",num1, num2);
    }
}
