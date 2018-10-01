import { EasyClientForBrowser } from '@uniqys/easy-client'



export default class SimpleStore {
  constructor() {
    this.client = new EasyClientForBrowser('http://localhost:3000')
  }
  async set(value) {
    await this.client.post('/api/set', { value }, { sign: true })
  }
  async get() {
    return await this.client.get('/api/get')
  }
}
