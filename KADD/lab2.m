f = @(x) (cosh(x)).^(-2);
xf = @(x) x*(cosh(x)).^(-2);
q = quadgk(f,-inf,inf)

dx = 0.001;
Y = -10:dx:10;
X = -10:dx:10;

t = trapz(Y,f(Y));
C_q = 1/q
C_t = 1/t

s = sum(f(Y));
C_s = 1/(s*dx)

funkcja = @(x) (1/q)*(cosh(x)).^(-2); %funkcja rozkładu

xfunkcja = @(x) x .* funkcja(x)
dystrybuanta =@(x) (1/2)*(tanh(x)+1);



oczekiwana_analityczna = 0 %wolframalpha
vari_analityczna = 3.141592^2/12 %tyż
stdn_analityczna = sqrt(vari_analityczna)

oczekiwana_calka = quadgk(xfunkcja, -inf, inf)
vari_calka = quadgk(@(x)(x-oczekiwana_calka).^2.*funkcja(x), -inf, inf)
std_calka = sqrt(vari_calka)

% oczekiwana = mean(funkcja(Y))
% mediana = median(funkcja(Y))
% stdn = std(funkcja(Y))
% vari = var(funkcja(Y))

moda = mode(funkcja(Y))




r = 0.25;
%kwantyl = @(r, x, y) ;
[c,i]=min(abs(dystrybuanta(Y)-r))
x_kwantyl1 = Y(i)
y_kwantyl1 = dystrybuanta(x_kwantyl1)

r = 0.5;
%kwantyl = @(r, x, y) ;
[c,i]=min(abs(dystrybuanta(Y)-r))
x_kwantyl2 = Y(i)
y_kwantyl2 = dystrybuanta(x_kwantyl2)

r = 0.75;
%kwantyl = @(r, x, y) ;
[c,i]=min(abs(dystrybuanta(Y)-r))
x_kwantyl3 = Y(i)
y_kwantyl3 = dystrybuanta(x_kwantyl3)

subplot(2,1,1)
hold on;
plot(Y,funkcja(Y))
title('funkcja')
xlabel('x')
ylabel('f(x)')
plot([oczekiwana_calka, oczekiwana_calka], [0,0.5], '-.r')
%plot([moda, moda], [0,0.5]) %niby line ale ARTYZM
hold off;

subplot(2,1,2)
hold on;
plot(Y, dystrybuanta(Y),'-.b',Y, (cumsum(funkcja(Y)))*dx, '*-r', Y, cumtrapz(X,funkcja(Y)), '.-g')
title('dystrybuanty')
xlabel('x')
ylabel('F(x)')
legend('analityczna', 'sum', 'trap')
tab_x1 = -10:dx:x_kwantyl1;
tab_y1 = dystrybuanta(tab_x1);
text(x_kwantyl1, y_kwantyl1, '<-25%')
area(tab_x1, tab_y1);
