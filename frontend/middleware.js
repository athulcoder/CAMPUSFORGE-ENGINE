import { NextResponse } from "next/server";

export function middleware(request) {
  const token = request.cookies.get("sessionId")?.value;
  const { pathname } = request.nextUrl;


    if (
    (pathname.startsWith("/login") ||
    pathname.startsWith("/register")) &&token) {
    return NextResponse.redirect(new URL("/dashboard", request.url));
  }
  // Allow public routes
  if (
    (pathname.startsWith("/login") ||
    pathname.startsWith("/register")) 
  ) {
    return NextResponse.next();
  }

  // Protect routes
  if (!token) {
    return NextResponse.redirect(new URL("/login", request.url));
  }

  return NextResponse.next();
}

export const config = {
  matcher: [
    "/((?!_next|api|favicon.ico|.*\\.(?:svg|png|jpg|jpeg|gif|css|js|woff2)).*)",
  ],
};