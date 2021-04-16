
package Lorenz
    model LorenzX
      parameter Real sigma = 10;
      output Real x(start = 1);
      input Real y(start = 1);
    equation
      der(x) = sigma * (y - x);
      annotation(experiment(StartTime = 0.0, StopTime = 100.0, Tolerance = 0.000001));
    end LorenzX;

    model LorenzY
      parameter Real rho = 28;
      input Real x(start = 1);
      output Real y(start = 1);
      input Real z(start = 1);
    equation
      der(y) = x * (rho - z) - y;
      annotation(experiment(StartTime = 0.0, StopTime = 100.0, Tolerance = 0.000001));
    end LorenzY;

    model LorenzZ
      parameter Real beta = 8 / 3;
      input Real x(start = 1);
      input Real y(start = 1);
      output Real z(start = 1);
    equation
      der(z) = x * y - beta * z;
      annotation(experiment(StartTime = 0.0, StopTime = 100.0, Tolerance = 0.000001));
    end LorenzZ;
end Lorenz;
