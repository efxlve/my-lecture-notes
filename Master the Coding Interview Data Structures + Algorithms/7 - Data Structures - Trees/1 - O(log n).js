//https://stackoverflow.com/questions/2307283/what-does-olog-n-mean-exactly

// Level 0: 2^0 = 1;
// Level 1: 2^1 = 2;
// Level 2: 2^2 = 4;
// Level 3: 2^3 = 8;

// # of nodes = 2^h - 1;
// log nodes = steps;

// log 100 = 2;
// 10^2 = 100;

// O(log n) nedir diye soruyorsunuz. Bu, büyük O notasyonunda bir karmaşıklık sınıfıdır. Bir algoritmanın çalışma süresinin giriş boyutunun logaritması ile orantılı olduğu anlamına gelir. Örneğin, bir ikili arama algoritması O(log n) karmaşıklığına sahiptir, çünkü her adımda arama alanını yarıya indirir.

// O(log* n) ise “yinelenen logaritma” olarak adlandırılır. Bu, logaritma fonksiyonunun sonuç 1 veya daha küçük olana kadar tekrar tekrar uygulanması gereken sayıdır. Örneğin, log*(1024) = 4’tür, çünkü log(1024) = 10, log(10) = 1, log(1) = 0 ve log(0) tanımsızdır.
