export default function createInt8TypedArray(
  arrayLength,
  byteOffset,
  bytevalue,
) {
  if (byteOffset >= arrayLength) {
    throw new Error('Position outside range');
  }

  const dataView = new DataView(
    new ArrayBuffer(arrayLength),
    0,
    arrayLength,
  );

  dataView.setUint8(byteOffset, byteValue);
  return dataView;
}
