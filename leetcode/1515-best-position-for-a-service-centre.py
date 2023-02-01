"""1515. Best Position for a Service Centre

https://leetcode.com/problems/best-position-for-a-service-centre/

Solution:
–––––––––

1. Second order Newton's method + gradient descent and momentum with early stopping.
    * Second order approximation with Newton's Method for the first 1000 steps
    * Gradient descent with a clever learning rate decay schedule
    * Momentum while computing the gradients and hessian
    * Early stopping by comparing the average losses in the last 1000, to the previous 1000
    steps.
2. [Times out / fails for some test cases] First order gradient descent with learning rate
    tuning and momentum

See https://vishnu.uk/blogs/challenging-problems.html#gradient-descent-newtons-method-leetcode--1515
for details.
"""

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
            # For integral values the mean is the optimal value. I haven't
            # proven why this is so.
            return _euclidean_dist(xc=mean_x, yc=mean_y, positions=positions)
        else:
            # `grad_descent()` for first order or `newton()` for second order
            return newton(xc=mean_x, yc=mean_y, positions=positions)

def _euclidean_dist(xc, yc, positions):
    return sum(
        ((x-xc)**2 + (y-yc)**2) ** (0.5)
        for x, y in positions
    )

#####################################################################################
# Second order grad descent using Newton's method with momentum.
# 
# Derive both the gradient and hessian
#
# See the image in my blog for the derivation
# https://vishnu.uk/blogs/challenging-problems.html#gradient-descent-newtons-method-leetcode--1515
#####################################################################################

def newton(xc, yc, positions):
    track_loss = False
    # Tracking loss
    if track_loss:
        print("iter\txc\tyc\tLoss")
        prev_loss = _euclidean_dist(xc=xc, yc=yc, positions=positions)
        print(f"{0}\t{xc:.7f}\t{yc:.7f}\t{prev_loss:.7f}")
    # Optimise
    max_iter = 50_000
    losses = [None] * max_iter
    momentum = 0.99
    prev_grads = None
    # window over which we average loss to stop
    lwin = 100
    it = 0
    for it in range(max_iter):
        step = do_newton_step(
            xc=xc,
            yc=yc,
            positions=positions,
            iter=it,
            prev_grads=prev_grads,
            momentum=momentum,
        )
        xc, yc, prev_grads = step["xc"], step["yc"], step["grads"]
        losses[it] = _euclidean_dist(xc=xc, yc=yc, positions=positions)
        if track_loss and it % 1000 == 0:
            print(f"{it}\t{xc:.7f}\t{yc:.7f}\t{loss:.7f}")
        # Early stopping if we have converged
        if it > 1000 and _has_converged(losses=losses, lwin=lwin, it=it):
            break
    return losses[it-1]


def _has_converged(losses, it, lwin, thresh=1e-5):
    # avg(losses[it-100:]) - avg(losses[it-200:it])
    return abs(sum(losses[it-2*lwin:it-lwin])-sum(losses[it-lwin:it]))/lwin <= 1e-10


def do_newton_step(xc, yc, positions, iter, prev_grads, momentum):
    grads = None
    # start with newton's update and then switch to grad descent
    second_order = iter < 1000
    for x, y in positions:
        grads_i = _compute_grads(x=x, y=y, xc=xc, yc=yc, second_order=second_order)
        # We sum up the gradients from all the positions
        if grads is None:
            grads = grads_i
        else:
            for k in grads:
                grads[k] += grads_i[k]
    grads = _smooth_grads(grads=grads, prev_grads=prev_grads, momentum=momentum)
    update = _compute_newton_update(grads=grads, iter=iter, second_order=second_order)
    return {
        "xc": xc + update["x_delta"],
        "yc": yc + update["y_delta"],
        "grads": grads,
    }


def _compute_grads(x, y, xc, yc, second_order=True):
    z = (xc-x)**2 + (yc-y)**2
    z_inv_1by2, z_inv_3by2 = z ** (-0.5), z ** (-1.5)
    xdiff, ydiff = (xc-x), (yc-y)
    # dx = (xc-xi) * z^(-1/2)
    dx, dy = xdiff * z_inv_1by2, ydiff * z_inv_1by2
    if not second_order:
        return {"dx": dx, "dy": dy, "dxx": 0., "dxy": 0., "dyy": 0.}
    # dxx = z^(-1/2) - (xc-xi)^2 * z^(-3/2)
    dxx = z_inv_1by2 - ((xdiff**2) * z_inv_3by2)
    dyy = z_inv_1by2 - ((ydiff**2) * z_inv_3by2)
    # dxy = (xc-xi) * (yc-yi) * z_inv_3by2
    dxy = xdiff * ydiff * z_inv_3by2
    return {
        "dx": dx,
        "dy": dy,
        "dxx": dxx,
        "dxy": dxy,
        "dyy": dyy,
    }

def _smooth_grads(grads, prev_grads, momentum):
    if prev_grads is None:
        return grads
    return {
        name: momentum * prev_grads[name] + (1-momentum) * cur_grad
        for name, cur_grad in grads.items()
    }

def _compute_newton_update(grads, iter, second_order, newton_lr=0.05):
    g = grads  # simplify further operations
    dx, dy, dxx, dxy, dyy = (g["dx"], g["dy"], g["dxx"], g["dxy"], g["dyy"])
    grad_lr = grad_desc_lr_schedule(it=iter)
    if not second_order:
        return _grad_update_helper(dx=dx, dy=dy, lr=grad_lr)
    try:
        return _newton_update_helper(dx=dx, dy=dy, dxx=dxx, dxy=dxy, dyy=dyy, lr=newton_lr)
    except ZeroDivisionError:
        # Hessian is not invertible do gradient update instead
        return _grad_update_helper(dx=dx, dy=dy, lr=grad_lr)

def grad_desc_lr_schedule(it):
    schedule = {
        (0, 2000): 0.1,
        (2000, 4000): 1e-2,
        (4000, 6000): 1e-3,
        (4000, 6000): 1e-4,
        (4000, float('inf')): 1e-8,
    }
    for (minv, maxv), lr in schedule.items():
        if minv <= it < maxv:
            return lr

def _newton_update_helper(dx, dy, dxx, dxy, dyy, lr):
    k = -1 / (dxx * dyy - (dxy**2))
    return {
        "x_delta": lr * k * (dyy * dx - dxy * dy),
        "y_delta": lr * k * (dxx * dy - dxy * dx),
    }

def _grad_update_helper(dx, dy, lr):
    return {"x_delta": -lr * dx, "y_delta": -lr * dy}

#####################################################################################
# First order grad descent with momentum
#####################################################################################
def grad_descent(xc, yc, positions):
    n = len(positions)
    max_iter = 50_000
    it = 0
    momentum = 0.99
    losses = [None] * max_iter
    lwin = 1000
    xgrad_buf, ygrad_buf = None, None
    for it in range(max_iter):
        xgrad = ygrad = total_dist = 0
        lr = learning_rate_schedule(it=it)
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
        losses[it] = total_dist
        if it > 1000 and _has_converged(losses=losses, lwin=lwin, it=it):
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


def learning_rate_schedule(it):
    schedule = {
        (0, 1000): 1.,
        (1000, 2000): 0.5,
        (2000, 4000): 0.1,
        (4000, 6000): 1e-3,
        (4000, 6000): 1e-4,
        (4000, float('inf')): 1e-8,
    }
    for (minv, maxv), lr in schedule.items():
        if minv <= it < maxv:
            return lr
