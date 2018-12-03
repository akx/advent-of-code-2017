const R = require('ramda');
const unfold2 = R.curryN(2, (fn, seed) => { // Like R.unfold, but passing the sequence being built
  const result = [];
  let pair = fn(seed, result);
  while (pair && pair.length) {
    result[result.length] = pair[0];
    pair = fn(pair[1], result);
  }
  return result;
});
const setIndex = (index, value) => R.set(R.lensIndex(index), value);
const incrIndex = (index) => R.over(R.lensIndex(index), R.inc);
const findMaxIndex = (arr) => R.findIndex(R.equals(R.reduce(R.max, 0, arr)))(arr);
const nextStep = (banks, index) => (index + 1) % banks.length;
const distStep = (banks, index, remaining) => (remaining <= 0 ? banks : distStep(incrIndex(index)(banks), nextStep(banks, index), remaining - 1));
const dist = (banks, index) => distStep(setIndex(index, 0)(banks), nextStep(banks, index), banks[index]);
const distMax = (banks) => dist(banks, findMaxIndex(banks));
const dup = (n => [n, n]);
const log = R.tap((obj) => console.log(obj));
const reallocate = unfold2((banks, seq) => R.any(R.equals(banks))(R.init(seq)) ? false : dup(distMax(banks)));

// --- //

const input = [5, 1, 10, 0, 1, 7, 13, 14, 3, 12, 8, 10, 7, 12, 0, 6];
const seq = reallocate(input);
console.log(seq.length);
