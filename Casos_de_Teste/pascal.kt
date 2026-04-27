fun main() {
    var n: Int = 5;
    var i: Int = 0;
    
    if (n < 1) {
        println("Erro: n deve ser maior que 0");
    } else {
        while (i < n) {
            var j: Int = 0;
            var num: Int = 1;
            
            while (j <= i) {
                println(num);
                num = num * (i - j) / (j + 1);
                j = j + 1;
            }
            i = i + 1;
        }
    }
}