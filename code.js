export function drawDot(ctx, x, y, r, color) {
  if (ctx != null) {
    ctx.save();
    ctx.beginPath();
    ctx.fillStyle = color;
    ctx.arc(x, y, r, 0, Math.PI * 2, true);
    ctx.fill();
    ctx.restore();
  }
}

export function drawLine(ctx, sx, sy, ex, ey, color) {
  if (ctx != null) {
    ctx.save();
    ctx.beginPath();
    ctx.strokeStyle = color;
    ctx.moveTo(sx, sy);
    ctx.lineTo(ex, ey);
    ctx.stroke();
    ctx.restore();
  }
}

export function drawArrow(ctx, sx, sy, ex, ey, color) {
  if (ctx != null) {
    drawLine(ctx, sx, sy, ex, ey, color);
    
    let aWidth = 5;
    let aLength = 12;
    let dx = ex - sx;
    let dy = ey - sy;
    let angle = Math.atan2(dy, dx);
    let length = Math.sqrt(dx * dx + dy * dy);

    //두점 선긋기
    ctx.translate(sx, sy);
    ctx.rotate(angle);
    ctx.fillStyle = color;
    ctx.beginPath();

    //화살표 모양 만들기
    ctx.moveTo(length - aLength, -aWidth);
    ctx.lineTo(length, 0);
    ctx.lineTo(length - aLength, aWidth);
    
    ctx.fill();
    ctx.setTransform(1, 0, 0, 1, 0, 0);
  }
}

export function drawRoadGraph(ctx, graph) {
  // 각 노드를 순회하며 연결된 도로를 그림
  console.log(graph)
} 