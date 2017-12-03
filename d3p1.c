#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#define DELTA(x, y) ((((x) + 1) << 4) | ((y) + 1))
#define DELTAX(d) ((int)((d) >> 4) - 1)
#define DELTAY(d) ((int)((d) & 15) - 1)
static const uint8_t R = DELTA(1, 0);
static const uint8_t U = DELTA(0, -1);
static const uint8_t D = DELTA(0, +1);
static const uint8_t L = DELTA(-1, 0);

static void ulamSpiralSteps(uint8_t *dir, int *c) {
  #define NEXT(nDir, nC) { *dir = (nDir); *c = (nC); return; }
  if(*c == 0) NEXT(R, 1);
  if(*dir == R) NEXT(U, (*c));
  if(*dir == U) NEXT(L, (*c) + 1);
  if(*dir == L) NEXT(D, (*c));
  if(*dir == D) NEXT(R, (*c) + 1);
  #undef NEXT
  fprintf(stderr, "unrecognized input %d/%d", *dir, *c);
  exit(9);
}

int main(int argc, char **argv) {
  int x = 0, y = 0, c = 0, step = 1, target;
  uint8_t dir = 0;
  target = (argc > 1 ? atoi(argv[1]) : 361527);
  do {
    ulamSpiralSteps(&dir, &c);
    int dx = DELTAX(dir);
    int dy = DELTAY(dir);
    for(int i = 0; i < c && step < target; i++) {
      x += dx;
      y += dy;
      step++;
    }
  } while (step < target);
  printf("%d %d %d\n", step, x, y);
}
