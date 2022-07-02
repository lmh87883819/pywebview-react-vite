const filePathPort = import.meta.env.DEV ? 'http://localhost:5000/file?path=' : `http://${window.location.host}/`;

export const file = (path) => {
  return filePathPort + path;
};
