#  TODO - Install dependencies?
wasm-pack build; cd www && npm run build; cd .. && docker build -t games-of-life .
