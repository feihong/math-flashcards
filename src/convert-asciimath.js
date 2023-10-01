{
  // Convert AsciiMath chunks to TeX chunks
  const convert = (str) => {
    return str
      .replace(/```([^`]+)```/g, (_match, group1) => '\\[' + window.AMTparseAMtoTeX(group1) + '\\]')
      .replace(/`([^`]+)`/g, (_match, group1) => '\\(' + window.AMTparseAMtoTeX(group1) + '\\)')
  }

  for (const cardEl of document.querySelectorAll('.math-1f960074-6883-4e97-b1bd-1bbfd36be0cb')) {
    cardEl.innerHTML = convert(cardEl.innerHTML);
  }
}
