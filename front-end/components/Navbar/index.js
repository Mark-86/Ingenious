import Link from "next/link";

const Navbar = () => {
  return (
    <nav className="fixed top-0 left-0 w-screen flex items-center justify-around py-5 z-50">
      <h1 className="gradientText text-3xl">Ingenious</h1>
      <ul className="flex text-white gap-x-10 items-center">
        <li className="hover:gradientBg transition-all px-8 py-2 rounded-3xl cursor-pointer">
          Home
        </li>
        <li className="hover:gradientBg px-8 py-2 transition duration-500 rounded-3xl cursor-pointer">
          About Us
        </li>

        <Link href="/auth">
          <a className="gradientBg px-8 py-2 rounded-3xl font-bold cursor-pointer">
            Login
          </a>
        </Link>
      </ul>
    </nav>
  );
};

export default Navbar;
