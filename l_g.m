%% Initialization
clear ; close all; clc

%% Load Data
fprintf('loading data\n');
data = load('tr_data.txt');
X = data(:, [1, 2,3,4,5,6,7,8,9,10,11,12,13,14,15]); y = data(:, 16);

[m, n] = size(X);



% Add intercept term to x and X_test
X = [ones(m, 1) X];

% Initialize fitting parameters
initial_theta = zeros(n + 1, 1);
fprintf('start calculating cost and grad\n');
lambda = 1
% Compute and display initial cost and gradient
[cost, grad] = costFunctionReg(initial_theta, X, y, lambda);
fprintf(' %f \n', grad);



%  Set options for fminunc
options = optimset('GradObj', 'on', 'MaxIter', 600);

%  Run fminunc to obtain the optimal theta
%  This function will return theta and the cost

lambda = 1
[theta, cost] = ...
	fminunc(@(t)(costFunctionReg(t, X, y,lambda)), initial_theta, options);

% Print theta to screen
fprintf('Cost at theta found by fminunc: %f\n', cost);
fprintf('theta: \n');
fprintf(' %f \n', theta);


% Compute accuracy on our training set
p = predict(theta, X);

fprintf('Train Accuracy: %f\n', mean(double(p == y)) * 100);

fprintf('Generate output.txt for test.\n');

tdata = load('tr_test.txt');
tX = tdata(:, [1, 2,3,4,5,6,7,8,9,10,11,12,13,14,15]); ty = tdata(:, 16);
[m, n] = size(tX);
tX = [ones(m, 1) tX];

tp =predict(theta, tX);
fid = fopen('output.txt','wt');
fprintf(fid, 'Id,solved_status\n');
fclose(fid);
tm = [ty,tp];
csvwrite('output.txt',tm,'-append');
