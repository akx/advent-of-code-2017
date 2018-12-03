function* ulamSpiralSteps() {
  let c = 1;
  for (; ;) {
    yield ['r', c];
    yield ['u', c];
    c++;
    yield ['l', c];
    yield ['d', c];
    c++;
  }
}

const dirToDelta = { 'r': [1, 0], 'u': [0, -1], 'l': [-1, 0], 'd': [0, 1] };

function* walkCoordinates(stepGenerator, x = 0, y = 0) {
  for (; ;) {
    const { value, done } = stepGenerator.next();
    if (done) break;
    const [dir, count] = value;
    const [dx, dy] = dirToDelta[dir];
    for (let i = 0; i < count; i++) {
      x += dx;
      y += dy;
      yield [x, y];
    }
  }
}

function* islice(generator, start, stop) {
  for (let step = 0; step < stop; step++) {
    const { value, done } = generator.next();
    if (done) break;
    if (step >= start && step < stop) {
      yield value;
    }
  }
}

function ifor(generator, callback) {
  for (let step = 0; ; step++) {
    const { value, done } = generator.next();
    if (done) break;
    if (callback(value, step) === false) break;
  }
}

function ilast(generator) {
  return new Promise((resolve) => {
    let value;
    for (; ;) {
      const rv = generator.next();
      if (rv.done) break;
      value = rv.value;
    }
    resolve(value);
  });
}

ilast(islice(walkCoordinates(ulamSpiralSteps()), 0, 361527 - 1)).then(([x, y]) => {
  console.log(x, y, Math.abs(x) + Math.abs(y));
});
