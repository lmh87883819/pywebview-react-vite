const filePathPort = import.meta.env.DEV ? 'http://localhost:5001/file?path=' : `http://${window.location.host}/`;

export const file = (path) => {
  return filePathPort + encodeURIComponent(path);
};
