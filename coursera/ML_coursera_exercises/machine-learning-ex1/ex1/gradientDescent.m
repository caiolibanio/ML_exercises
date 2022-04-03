function [theta, J_history] = gradientDescent(X, y, theta, alpha, num_iters)
%GRADIENTDESCENT Performs gradient descent to learn theta
%   theta = GRADIENTDESCENT(X, y, theta, alpha, num_iters) updates theta by 
%   taking num_iters gradient steps with learning rate alpha

% Initialize some useful values
m = length(y); % number of training examples
J_history = zeros(num_iters, 1);


temp1 = 0;
temp2 = 0;


for iter = 1:num_iters,
  
  %t1 = (theta'*X') - y;
  %t1 = t1 / m;
  
  %theta(1) = theta(1) - ((((theta'*X') - y) / m) * alpha);
  %theta(2) = theta(2) - (((((theta'*X') - y) / m) * alpha) * X(:,2));
  temp1 = 0;
  temp2 = 0;
  
  h = X * theta;
  for i = 1:rows(X),
    temp1 = temp1 + (h(i) - y(i));
    temp2 = temp2 + (h(i) - y(i)) * X(i, 2);
    % ====================== YOUR CODE HERE ======================
    % Instructions: Perform a single gradient step on the parameter vector
    %               theta. 
    %
    % Hint: While debugging, it can be useful to print out the values
    %       of the cost function (computeCost) and gradient here.
    %
    % ============================================================

    % Save the cost J in every iteration    
    
  end
  temp1 = theta(1) - ((temp1 / m) * alpha);
  temp2 = theta(2) - ((temp2 / m) * alpha);
  
  theta(1) = temp1;
  theta(2) = temp2;
  
  J_history(iter) = computeCost(X, y, theta);
end

end
