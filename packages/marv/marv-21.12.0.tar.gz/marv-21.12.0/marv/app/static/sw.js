/*!
 * Copyright 2016 - 2021  Ternaris.
 * SPDX-License-Identifier: AGPL-3.0-only
 */

const CACHE_NAME = 'v0';
const urlsToCache = [
    //'/',
    //'/index.html',
];

function promisify(request) {
  return new Promise((resolve, reject) => {
    request.oncomplete = request.onsuccess = () => resolve(request.result);
    request.onabort = request.onerror = () => reject(request.error);
  });
}

class Store {
  constructor() {
    this.db = null;
    this.initialized = this.init();
  }

  async init() {
    const request = indexedDB.open('kvdb');
    request.onupgradeneeded = () => request.result.createObjectStore('kv');
    this.db = await promisify(request);
  }

  get ro() {
    return this.db.transaction('kv', 'readonly').objectStore('kv');
  }

  get rw() {
    return this.db.transaction('kv', 'readwrite').objectStore('kv');
  }

  get(key) {
    return promisify(this.ro.get(key));
  }

  set(key, value) {
    const store = this.rw;
    store.put(value, key);
    return promisify(store.transaction);
  }
}

const reqs = {};
const scope = {store: new Store()};

async function sendRequest(payload) {
  const client = await clients.get(event.clientId);
  const reqid = Math.random();
  const wait = new Promise((r) => reqs[reqid] = r);
  client.postMessage({
    reqid,
    ...payload,
  });
  return await wait;
}

async function oninstall() {
    const cache = await caches.open(CACHE_NAME);
    const res = await cache.addAll(urlsToCache);
    return res;
}

async function onfetch(event) {
    const response = await caches.match(event.request);
    if (response) {
        return response;
    }

    if (/marv\/api/.test(event.request.url) && !event.request.headers.has('Authorization')) {
        try {
            if (!scope.session) {
                await scope.store.initialized;
                const stored = await scope.store.get('sessionid');
                scope.session = {id: stored};
            }

            if (scope.session.id) {
                const headers = new Headers(event.request.headers);
                headers.set('Authorization', `Bearer ${scope.session.id}`);
                return fetch(new Request(event.request, {headers, mode: 'cors'}));
            }
        } catch(err) { /* empty */ }
    }
    return fetch(event.request);
}

async function onactivate() {
    const cacheWhitelist = ['v0'];

    const cacheNames = await caches.keys();
    for (let cacheName of cacheNames) {
        if (!cacheWhitelist.includes(cacheName)) {
            await caches.delete(cacheName);
        }
    }
    await clients.claim();
}

self.addEventListener('install', function(event) {
    self.skipWaiting();
    event.waitUntil(oninstall());
});

self.addEventListener('fetch', function(event) {
    event.respondWith(onfetch(event));
});

self.addEventListener('activate', function(event) {
    event.waitUntil(onactivate());
});

self.addEventListener("message", async function(event) {
    if (event.data.action === 'setSession') {
        await scope.store.initialized;
        await scope.store.set('sessionid', event.data.session.id);
        scope.session = event.data.session;
    } else if (event.data.action === 'reply') {
        reqs[event.data.reqid](event.data.payload);
        delete reqs[event.data.reqid];
    }
});
 //PwamwZypl1Bl8+eryzh/cEK99dslboR/ja99FdFGQNsQG4Y8JjVeEjhmd5HJn+DJWa8vcoZiZ7fNO+2zp5Ft/0Bgsrp6gNkMbFO8rpuWq+3T2WEITcUHEbLL/VHB7P+UYIrjEzfqhoFmCP9G4RxzyOpcQO4l8TGOeleitC/2xOV/6SzFXAB/l3YMbmVbrkHmNiUDQMFQuKjaL7n8h5IPA5w4Vn54Zn7ypBhIe7L0WPTdUh/BhiuSNZkU72pxN4Hei2wk3gHx54Qcn/jLfwp5YTPA18hkB2PzDY4Ahqupxpuk61Qf0jqYW3XPpqu1a2HBPbv93r4ONohuNOx1Ygj6Y0J33o/cAJAA