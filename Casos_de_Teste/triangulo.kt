fun main() {
  var a: Int = 2;
  var b: Int = 3;
  var c: Int = 2;

  
  if (a <= 0 || b <= 0 || c <= 0) {
    println("Erro: Valores devem ser maiores que zero");
  } else {
      
    if ((a + b > c) && (a + c > b) && (b + c > a)) {
        
        
      if (a == b && b == c) {
        println("Triângulo equilátero válido");
      } else if (a == b || a == c || b == c) {
        println("Triângulo isósceles válido");
      } else {
        println("Triângulo escaleno válido");
      }
    } else {
      println("Medidas inválidas");
    }
  }
}