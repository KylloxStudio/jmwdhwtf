function drawBoard(ctx, canvas, boardSize, cellSize) {
  ctx.beginPath();
  for (let i = 0; i < boardSize; i++) {
    // 가로선 그리기
    ctx.moveTo(0, i * cellSize);
    ctx.lineTo(canvas.width, i * cellSize);

    // 세로선 그리기
    ctx.moveTo(i * cellSize, 0);
    ctx.lineTo(i * cellSize, canvas.height);
  }

  ctx.strokeStyle = "black"; // 선 색상
  ctx.stroke(); // 선 그리기
}

document.addEventListener("DOMContentLoaded", function() {
  const canvas = document.getElementById("boardCanvas");
  const ctx = canvas.getContext("2d");

  const boardSize = 12; // 도로 크기
  const cellSize = canvas.width / boardSize;

  ctx.fillText("(0, 0)", 20, 505);
  ctx.fillText("(10, 10)", 500, 40);

  drawBoard(ctx, canvas, boardSize, cellSize);
});
