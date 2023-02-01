"""1515. Best Position for a Service Centre

https://leetcode.com/problems/best-position-for-a-service-centre/

Solution:
Gradient descent with learning rate tuning and momentum
"""
import math

class Solution:
    def getMinDistSum(self, positions: List[List[int]]) -> float:
        mean_x, mean_y = 0., 0.
        for x, y in positions:
            mean_x += x
            mean_y += y
        n = len(positions)
        mean_x /= n
        mean_y /= n
        if mean_x.is_integer() and mean_y.is_integer():
            return _euclidean_dist(xc=mean_x, yc=mean_y, positions=positions)
        else:
            return grad_descent(xc=mean_x, yc=mean_y, positions=positions)

def _euclidean_dist(xc, yc, positions):
    return sum(
        math.sqrt( (x-xc)**2 + (y-yc)**2 )
        for x, y in positions
    )

def grad_descent(xc, yc, positions):
    n = len(positions)
    max_iter = 50_000
    prev_dist = 0
    it = 0
    momentum = 0.99
    xgrad_buf, ygrad_buf = None, None
    for it in range(max_iter):
        if it < 1000:
            lr = 1.
        elif 1000 <= it < 2000:
            lr = 0.5
        elif 2000 <= it < 4000:
            lr = 0.1
        elif 4000 <= it < 6000:
            lr = 0.001
        elif 6000 <= it < 10000:
            lr = 1e-4
        else:
            lr = 1e-8
        xgrad = ygrad = total_dist = 0
        for i, (x, y) in enumerate(positions):
            xdiff = (xc-x)
            ydiff = (yc-y)
            dist = (xdiff**2 + ydiff**2)**(0.5)
            total_dist += dist
            xgrad += xdiff / dist
            ygrad += ydiff / dist
        xgrad_buf = _update_grad(grad_buf=xgrad_buf, grad=xgrad, momentum=momentum)
        ygrad_buf = _update_grad(grad_buf=ygrad_buf, grad=ygrad, momentum=momentum)
        xc = xc - lr * xgrad
        yc = yc - lr * ygrad
        if abs(total_dist - prev_dist) < 1e-7:
            break
        else:
            prev_dist = total_dist
    return total_dist


def _update_grad(grad_buf, grad, momentum):
    if grad_buf is not None:
        grad_buf = momentum * grad_buf + (1-momentum) * grad 
    else:
        grad_buf = grad
    return grad_buf
