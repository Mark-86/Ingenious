import Link from "next/link";
import { FaArrowAltCircleRight } from "react-icons/fa";
const Main = () => {
  return (
    <div className="w-screen h-screen top-0 left-0 text-center flex flex-col gap-y-3 justify-center relative z-0 items-center ">
      <h1 className="gradientText text-8xl h-[110px]">Welcome to Ingenious</h1>
      <p className="text-gray-300 text-2xl ">
        Our community allows you to become the best coder of yourself!
      </p>
      <Link href={"codeground"}>
        <div className="gradientBg cursor-pointer rounded-full px-10 text-2xl mt-5 py-5 flex items-center justify-between">
          <button className="font-extrabold text-white mr-10">
            Get Started
          </button>
          <div>
            <FaArrowAltCircleRight size={24} color={"white"} />
          </div>
        </div>
      </Link>
    </div>
  );
};

export default Main;
