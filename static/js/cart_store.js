// Simple cart store (localStorage)
const CART_KEY = 'foodie_cart_v1';
export function getCart(){ return JSON.parse(localStorage.getItem(CART_KEY)||'[]'); }
export function saveCart(cart){ localStorage.setItem(CART_KEY, JSON.stringify(cart)); }
